#打开
E:
cd E:\PythonT\myscript
conda activate mask1
jupyter notebook

#配置nbextensions
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib-nbextension install --user
jupyter notebook

#配置虚拟环境
conda create -n mask1 python=3.8 #虚拟环境名为mask1
conda activate mask1
pip install requests #安装requests包
conda install ipykernel
python -m ipykernel install --user --name mask1 --display-name mask1
pip install notebook

