from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite

def main():
    if __name__ == "__main__":
        root = MindMapComposite("The Twilight Zone", "circle")

        characters = MindMapComposite("Characters", "oval")
        characters.add(MindMapLeaf("Rod Serling", "plain"))
        characters.add(MindMapLeaf("William Shatner", "plain"))
        characters.add(MindMapLeaf("Burgess Meredith", "plain"))
        characters.add(MindMapLeaf("Anne Francis", "plain"))
        characters.add(MindMapLeaf("Robert Redford", "plain"))
        root.add(characters)

        plot_points = MindMapComposite("Plot Points", "square")
        plot_points.add(MindMapLeaf("Stories explore moral, philosophical, and social issues", "plain"))
        plot_points.add(MindMapLeaf("Often features ironic twists or surprises", "plain"))
        plot_points.add(MindMapLeaf("Episodes blend science fiction, fantasy, and horror", "plain"))
        plot_points.add(MindMapLeaf("Focus on the darker and unpredictable side of human nature", "plain"))
        root.add(plot_points)

        themes = MindMapComposite("Themes", "cloud")
        themes.add(MindMapLeaf("The consequences of hubris", "plain"))
        themes.add(MindMapLeaf("The fear of the unknown", "plain"))
        themes.add(MindMapLeaf("Social isolation and loneliness", "plain"))
        themes.add(MindMapLeaf("Humanity's struggle with morality", "plain"))
        root.add(themes)

        setting = MindMapComposite("Setting", "hexagon")
        setting.add(MindMapLeaf("Unfamiliar small towns", "plain"))
        setting.add(MindMapLeaf("Isolated places (airplanes, remote areas)", "plain"))
        setting.add(MindMapLeaf("Alien worlds or dystopian futures", "plain"))
        setting.add(MindMapLeaf("Ordinary locations with surreal twists", "plain"))
        root.add(setting)

        conflicts = MindMapComposite("Major Conflicts", "bang")
        conflicts.add(MindMapLeaf("Humans vs. their own fears and flaws", "plain"))
        conflicts.add(MindMapLeaf("Humans vs. supernatural or otherworldly forces", "plain"))
        conflicts.add(MindMapLeaf("Social norms vs. individuality", "plain"))
        root.add(conflicts)

        dialogue = MindMapComposite("Dialogue Highlights", "oval")
        dialogue.add(MindMapLeaf("There is a fifth dimension beyond that which is known to man.", "plain"))
        dialogue.add(MindMapLeaf("You’re traveling through another dimension...", "plain"))
        dialogue.add(MindMapLeaf("This is the dimension of imagination.", "plain"))
        root.add(dialogue)

        stage_directions = MindMapComposite("Significant Stage Directions", "square")
        stage_directions.add(MindMapLeaf("Use of dramatic lighting and shadows", "plain"))
        stage_directions.add(MindMapLeaf("Frequent use of twist endings", "plain"))
        stage_directions.add(MindMapLeaf("Minimalistic sets to focus on storytelling", "plain"))
        root.add(stage_directions)

        # Display the Mind Map
        root.display()


if __name__ == "__main__":
    main()