#!/usr/bin/env python
from dna_features_viewer import BiopythonTranslator, CircularGraphicRecord
import matplotlib.pyplot as plt
from matplotlib import rc

class Translator(BiopythonTranslator):
    
    def compute_feature_color(self, feature):
        color_map = {
            "source": "black",
            "CDS": "yellow",
            "gene": "darkblue",
        }
        
        return color_map[feature.type]
    
    def compute_feature_box_color(self, feature):
        color_map = {
            "source": "white",
            "CDS": "lightyellow",
            "gene": "lightblue",
        }
        
        return color_map[feature.type]
    
    def compute_feature_label(self, feature):
        if feature.type == "CDS": # not sure if we need to label the gene as well, can be changed if needed
            return BiopythonTranslator.compute_feature_label(self, feature)
        return None

def draw():
    """Create record and plot it"""
    fig, ax = plt.subplots()
    rec = Translator().translate_record("Genome.gb", record_class="circular")
    rec.plot(ax=ax, figure_width=10, strand_in_label_threshold=4)
    plt.title("Tomato Curly Stunt Virus, Genome Map")
    plt.savefig("genome_map.png", bbox_inches="tight")
    
if __name__ == "__main__":
    rc('text', usetex=True)
    draw()
