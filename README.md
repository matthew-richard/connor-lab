# connor-lab
Notes and Blender prototypes from my time working at Dr. Ed Connor's JHU lab for researching the mammalian visual cortex.

The most interesting files in this repo are the Blender Python scripts in `blender/firstsim/scripts`, which automatically set up a physics sim, run it, and then render the result using Blender's ray tracing engine. This was applicable to Dr. Connor's work, since his lab was interested in determining whether certain neurons were specialized to detect physically stable (i.e. firmly planted on the ground, not precarious) object scenes, as opposed to physically unstable ones (e.g. a cube resting on one of its corners).

Dr. Connor had formerly been using an OpenGL and Java based implementation to generate scenes entirely programmatically. Switching to Blender scripts would have allowed for manual coarse control over the images produced (via manipulation of the scene in the Blender GUI) while allowing for programmatic modification, which was necessary for the the lab's [evolutionary algorithms](https://en.wikipedia.org/wiki/Evolutionary_algorithm) to measure neurological responses to various image stimuli and then tweak those stimuli accordingly.

If you open a Python console in the `firstsim/test.blend` file, you can see some of the Python commands that I experimented with, including commands that directly manipulated the geometry of the scene objects. E.g. `bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0` moves the X coordinate of the first vertex of the object named "Cube" 1 unit in the +X direction.

