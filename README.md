# connor-lab
Notes and Blender prototypes from time working at Dr. Ed Connor's JHU lab for researching the mammalian visual cortex.

`blender/physicssim.blend` contains some early experiments in how I might have replaced Dr. Connor's OpenGL-based paremterized image generation software with something Blender-based, which would have allowed more intuitive high-level control over the images produced (via manipulation of the scene in the Blender GUI) while still allowing them to programmatically modifiable (which was required for Dr. Connor's use of evolutionary algorithms to measure neurological responses to various image stimuli) via Python scripting.

E.g. it's much quicker to set up a basic physics sim via the Blender GUI vs doing it programmatically in Java using a game engine library like [LWJGL](https://www.lwjgl.org/), which is what lab had been using. You can then trigger the sim to run programmatically.

If you open a Python console in the `firstsim/test.blend` file, you can see some of the Python commands that I experimented with, including commands that directly manipulated the geometry of the scene objects. E.g. `bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0` moves the X coordinate of the first vertex of the object named "Cube" 1 unit in the +X direction.

