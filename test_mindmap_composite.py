from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

root = MindMapComposite("Root", "circle")
leaf1 = MindMapLeaf("Leaf1", "square")
leaf2 = MindMapLeaf("Leaf2", "cloud")
root.add(leaf1)
root.add(leaf2)

print(str(root))
root.display()

print("MindMapComposite tests completed!")