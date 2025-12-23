import matplotlib.pyplot as plt
import pandas as pd

def create_table_image():
    data = [
        [3, 0, '3072 – 3103'],
        [2, 4, '2176 – 2207'],
        [0, 5, '160 – 191'],
        [0, 7, '224 – 255']
    ]
    columns = ['Tag', 'Index', 'Data Address Range (start – end)']
    df = pd.DataFrame(data, columns=columns)
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     loc='center',
                     cellLoc='center')
  
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.5)
    header_color = '#a6b9d6'
    row_color = '#e6e6e6'
  
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor(header_color)
            cell.set_text_props(weight='bold')
        else:
            cell.set_facecolor(row_color)
        cell.set_edgecolor('black')
        cell.set_linewidth(1)
      
    title_text = "Τελική Κατάσταση Κρυφής Μνήμης\n< Tag, Index, Address Range >"
    plt.title(title_text, fontsize=14, fontweight='bold', y=1.3, loc='center')
    output_filename = 'cache_table_recreated.png'
    plt.savefig(output_filename, bbox_inches='tight', pad_inches=0.5, dpi=300)
    print(f"Image successfully generated and saved as '{output_filename}'")

if __name__ == "__main__":
    create_table_image()
