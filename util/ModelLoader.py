from pyglet.gl import *
import ctypes
import pyrr
import time
import numpy
from util.ObjLoader import ObjLoader
import util.ShaderLoader as ShaderLoader

class ModelLoader:
    def __init__(self, res):

        self.mesh = ObjLoader()
        self.mesh.load_model(res)

        num_verts = len(self.mesh.model_vertices) // 3

        self.verts = pyglet.graphics.vertex_list(num_verts, ('v3f', self.mesh.model_vertices),
                                                            ('t2f', self.mesh.model_textures),
                                                            ('n3f', self.mesh.model_normals))

        shader = ShaderLoader.compile_shader("model_vert", "model_frag")

        glUseProgram(shader)

        # vertices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, self.verts.vertices)
        glEnableVertexAttribArray(0)
        # textures
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, self.verts.tex_coords)
        glEnableVertexAttribArray(1)
        # normals
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 0, self.verts.normals)
        glEnableVertexAttribArray(2)

        projection = pyrr.matrix44.create_perspective_projection_matrix(45.0, 1280 / 720, 0.1, 100.0).flatten().astype("float32")
        view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -2.0])).flatten().astype("float32")
        model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -1.0])).flatten().astype("float32")

        c_projection = numpy.ctypeslib.as_ctypes(projection)
        c_view = numpy.ctypeslib.as_ctypes(view)
        c_model = numpy.ctypeslib.as_ctypes(model)

        view_loc = glGetUniformLocation(shader, b"view")
        proj_loc = glGetUniformLocation(shader, b"projection")
        self.model_loc = glGetUniformLocation(shader, b"model")
        self.rotate_loc = glGetUniformLocation(shader, b'rotate')
        self.light_loc = glGetUniformLocation(shader, b"light")

        glUniformMatrix4fv(view_loc, 1, GL_FALSE, c_view)
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, c_projection)
        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, c_model)

        # texture settings and loading
        texture = GLuint(0)
        glGenTextures(1, texture)
        glBindTexture(GL_TEXTURE_2D, texture)
        # set the texture wrapping
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # set the texture filtering
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # xmas = pyglet.image.load('../models/monkey.jpg')
        # image_data = xmas.get_data('RGB', xmas.pitch)
        # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, xmas.width, xmas.height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

    def rotate(self, rotation):

        self.rot_y = pyrr.Matrix44.from_y_rotation(rotation).flatten()

        c_rotate = (GLfloat * len(self.rot_y))(*self.rot_y)

        glUniformMatrix4fv(self.rotate_loc, 1, GL_FALSE, c_rotate)
        glUniformMatrix4fv(self.light_loc, 1, GL_FALSE, c_rotate)

    def translate(self, position):
        translation = [position.x, position.y, position.z]

        self.trans = pyrr.Matrix44.from_translation(translation).flatten()
        c_translate = (GLfloat * len(self.trans))(*self.trans)

        glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, c_translate)
