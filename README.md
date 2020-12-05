# connor-lab
Notes and Blender prototypes from time working at Dr. Ed Connor's JHU lab for researching the mammalian visual cortex.

The most interesting files in this repo are the ones `blender/firstsim/scripts`, which are some Blender Python scripts for automatically setting up a physics sim, running it, and then rendering this result. This was applicable to Dr. Connor's work, since his lab was interested in determining whether certain neurons specialized in detecting physically stable (i.e. firmly planted on the ground, not precarious) object scenes, vs physically unstable ones (e.g. a cube resting on one of its corners).

Dr. Connor had formerly been using entirely programmatic, OpenGL-based scenes. Switching to Blender scripts would have allowed more intuitive high-level control over the images produced (via manipulation of the scene in the Blender GUI) while still allowing them to be programmatically modifiable (which was required for Dr. Connor's use of evolutionary algorithms to measure neurological responses to various image stimuli) via Python scripting.

E.g. it's much quicker to set up a basic physics sim via the Blender GUI vs doing it programmatically in Java using a game engine library like [LWJGL](https://www.lwjgl.org/), which is what lab had been using. You can then trigger the sim to run programmatically.

If you open a Python console in the `firstsim/test.blend` file, you can see some of the Python commands that I experimented with, including commands that directly manipulated the geometry of the scene objects. E.g. `bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0` moves the X coordinate of the first vertex of the object named "Cube" 1 unit in the +X direction.

