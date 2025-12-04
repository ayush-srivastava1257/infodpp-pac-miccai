def test_imports():
    print("Testing imports...")
    import torch
    import yaml
    try:
        # Attempt to import config loader if it exists
        from infodpp.utils.config import load_config
        print("Config loader OK")
    except ModuleNotFoundError:
        print("Config loader not found yet, skipping...")
    print("Imports OK")

def test_gpu():
    import torch
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
    print("GPU test OK")

if __name__ == "__main__":
    test_imports()
    test_gpu()
