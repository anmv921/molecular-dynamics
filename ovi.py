# -*- coding: utf-8 -*-
"""
Spyder Editor

Needs to be run from inside the ovitoenv conda environmennt
"""

from ovito.io import import_file
import os
from ovito.vis import Viewport
import math
from ovito.vis import ParticlesVis, TachyonRenderer

pipeline = import_file(os.path.join("2022-04-11-19.29.42.02", "ovito.xyz"))
data = pipeline.compute()
data.cell.vis.enabled = True
data.cell.vis.rendering_color = (1,0,0)
data.particles.vis.shape = ParticlesVis.Shape.Circle

pipeline.add_to_scene()

vp = Viewport()
vp.type = Viewport.Type.Top
vp.zoom_all()

vp.render_image(filename="myimage.png", size=(800,600), frame=pipeline.source.num_frames,
                background=(0,0,0))

vp.render_anim(size=(800,600), filename="animation.avi", fps=20)