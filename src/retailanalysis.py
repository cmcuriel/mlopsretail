import hydra
import os
from omegaconf import DictConfig, OmegaConf

#@hydra.main(config_path="conf", config_name="retail_main_config", version_base=None)
#@hydra.main(version_base=None)
@hydra.main(config_path="D:/MLOps/Trabajo Final/config/", config_name="retail_config", version_base=None)
def process_data(config: DictConfig)->None:
    #source = config.data.file
    #cols_to_drop = config.cols_to_drop_segmentation
    print(f"Working directory : {os.getcwd()}")
    print(f"Output directory  : {hydra.core.hydra_config.HydraConfig.get().runtime.output_dir}")
    print(OmegaConf.to_yaml(config))
    
if __name__ == "__main__":
    process_data()