from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

mc.postToChat('test')
mc.postToChat('Lava is %d' % block.LAVA.id)
mc.postToChat('TNT is %d' % block.TNT.id)

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 38)

def createUpstand(x,y,z):
    mc.setBlocks(x,y,z,x,y+8,z, block.WOOD.id)

def create_house():
    mc.setBlock(x-1,y+1,z, block.DOOR_WOOD.id)

    mc.setBlocks(x-2,y-1,z-4,x-10,y-1,z+4, block.STONE_BRICK.id)

    mc.setBlocks(x-1,y-1,z-5,x-1,y-1,z+5, block.STONE.id)
    mc.setBlocks(x-1,y-1,z-5,x-10,y-1,z-5, block.STONE.id)
    mc.setBlocks(x-10,y-1,z-5,x-10,y-1,z+5, block.STONE.id)
    mc.setBlocks(x-10,y-1,z+5,x-1,y-1,z+5, block.STONE.id)

    createUpstand(x-1,y-1,z-5)
    createUpstand(x-1,y-1,z+5)
    createUpstand(x-10,y-1,z-5)
    createUpstand(x-10,y-1,z+5)

def clear_construction_area():
