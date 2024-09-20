from pydantic_settings import BaseSettings


class PatchExtractionSettings(BaseSettings):
    source: str
    step_size: int = 256
    patch_size: int = 256
    patch: bool = True
    seg: bool = True
    stitch: bool = True
    no_auto_skip: bool = True
    save_dir: str = "../artifacts/"
    preset: str | None = None
    patch_level: int = 0
    custom_downsample: int = 1
    process_list: str | None = None


class FeatureExtractionSettings(BaseSettings):
    data_h5_dir: str
    data_slide_dir: str
    csv_path: str
    feat_dir: str
    slide_ext: str = ".svs"
    model: str = "resnet50_trunc"
    batch_size: int = 256
    no_auto_skip: bool = False
    target_patch_size: int = 224


if __name__ == "__main__":
    config = PatchExtractionSettings()
    print(config)
