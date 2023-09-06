### How to activate the virtual environment (https://github.com/AutodeskAILab/Building-GAN/issues/9)
conda create -n "venv" python=3.8
conda activate venv
conda deactivate

export PATH=~/anaconda3/bin:$PATH

### Installed libraries
* export PYTHONPATH=:/Downloads/Thèse\ GenH2Arch/Implementations/Building-GAN/
* Don't have a GPU in the testing machine
* pip install torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
* pip install torch-scatter -f https://pytorch-geometric.com/whl/torch-1.8.0+cpu.html
* pip install torch-sparse -f https://pytorch-geometric.com/whl/torch-1.8.0+cpu.html
* pip install torch-cluster -f https://pytorch-geometric.com/whl/torch-1.8.0+cpu.html
* pip install torch-spline-conv -f https://pytorch-geometric.com/whl/torch-1.8.0+cpu.html
* pip install torch-geometric==1.6.2

