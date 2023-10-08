import env
from modules.helper_methods import dprint
from modules.setup import setup
from modules.heatmap_handler import capture_heatmap
from modules.gpuconfig_handler import downscale_gpuconfig
from modules.select_chunks import select_chunks
from modules.select_sections import select_sections
from modules.helper_methods import visualize_selected_pixels
from modules.script_handler import setup_script_env
from modules.script_handler import run_tracer_script
from modules.results_handler import fetch_results


if __name__ == '__main__':
    setup()
    capture_heatmap()
    # downscale_gpuconfig()
    #
    # for i in range(env.configs.num_chunks):
    #     valid_coords = select_chunks(i)
    #     for k in range(env.configs.iterations):
    #         out_coords = f"data/coordinates/chunk_{i}_{k}.coords"
    #         select_sections(valid_coords, out_coords)
    #
    #         if env.configs.debug:
    #             out_visualization = f"data/debug/chunk_{i}_{k}_visualize.png"
    #             visualize_selected_pixels(out_coords, out_visualization)
    #             dprint(env.plvl.info, f"Visualized chunk {i} {k}")

    # setup_script_env()
    # run_tracer_script()
    # fetch_results()