#version 330
in vec2 textures;
in vec3 fragNormal;

out vec4 outColor;
uniform sampler2D sampTexture;

void main()
{
    vec3 ambientLightIntensity = vec3(0.3f, 0.2f, 0.4f);
    vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
    vec3 sunLightDirection = normalize(vec3(1.0f, 1.0f, -0.5f));

    vec4 color = vec4(1.0f, 1.0f, 1.0f, 1.0f);

    vec3 lightIntensity = ambientLightIntensity + sunLightIntensity * max(dot(fragNormal, sunLightDirection), 0.0f);
    outColor = vec4(color.rgb * lightIntensity, 1.0f);
}