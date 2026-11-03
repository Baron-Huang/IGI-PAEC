# Instance Gradient-entropy Inhibition-optimized Prior-guiding Actively Explainable Clustering for Achieving Pathologist-like Grading
## 🧔 Authors [* is corresponding authors]
- Pan Huang, _Member_, _IEEE_, Mingrui Ma, Lan Wang, Zhiyong Li*, Qin Jin*, _Senior Member_, _IEEE_

## :fire: News
- [xxxx/xx/xxx] xxxx.



## :rocket: Pipeline
1. Here's a motivation of our **Instance Gradient-entropy Inhibition-optimized Prior-guiding Active Explanation Clustering (IGI-PAEC)** method:

<div align=center>
<img src="https://github.com/Baron-Huang/TicMIL/blob/main/Main_fig/Motivation_for_IGI_PAEC.jpg" style="width:100%; height:100%;">
</div>
   
2. Here's an overview of our **IGI-PAEC** method:

<div align=center>
<img src="https://github.com/Baron-Huang/TicMIL/blob/main/Main_fig/Main_Frame_for_IGI_PAEC.jpg" style="width:80%; height:80%;">
</div>


3. Here's a visually explainable result of our **IGI-PAEC** method:
<div align=center>
<img src="https://github.com/Baron-Huang/TicMIL/blob/main/Main_fig/Visual_for_IGI_PAEC.jpg" style="width:100%; height:100%;">
</div>


4. Here's a statistically explainable result of our **IGI-PAEC**
<div align=center>
<img src="https://github.com/Baron-Huang/TicMIL/blob/main/Main_fig/ICALE_ROC_IGI_PAEC.jpg" style="width:100%; height:100%;">
</div>


## :mag: TODO
<font color="red">**We are currently organizing all the code. Stay tuned!**</font>
- [x] training code
- [x] Evaluation code
- [x] Model code
- [ ] Pretrained weights
- [ ] Datasets





## 🛠️ Getting Started

To get started with **IGI-PAEC**, follow the installation instructions below.

1.  Clone the repo

```sh
git clone https://github.com/Baron-Huang/IGI_PAEC
```

2. Install dependencies
   
```sh
pip install -r requirements.txt
```

3. Training on Swin Transformer-S Backbone
```sh
sh IGI_PAEC_main.sh
Modify: --abla_type sota --run_mode train --random_seed ${seed}
```

4. Evaluation
```sh
sh IGI_PAEC_main.sh
Modify: --abla_type sota --run_mode test --random_seed ${seed}
```

5. Extract features for plots
```sh
sh IGI_PAEC_main.sh
Modify: --abla_type sota --run_mode test --random_seed ${seed} --feat_extract
```

6. Interpretability plots
```sh
sh IGI_PAEC_main.sh
Modify: --abla_type sota --run_mode test --random_seed ${seed} --bag_weight
```

## :gear: Training parameters for the additional datasets

The repository includes dataset-specific training entry points. The following
defaults reproduce the settings encoded in the corresponding scripts; update
the dataset and output paths for your local environment before running.

| Dataset | Entry point | Classes | Patch size | Batch size | Epochs | Bag length | Input length | GPUs |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | --- |
| DHMC-Kidney | `IGI_PAEC_main_DHMC_Kidney.py` | 5 | 224 x 224 | 1 | 100 | 2000 | 500 | 0, 1, 2 |
| AMU-LSCC | `IGI_PAEC_main_AMU_LSCC.py` | 3 | 96 x 96 | 1 | 100 | 2000 | 500 | 0, 2 |
| AMU-CSCC | `IGI_PAEC_main_AMU_CSCC.py` | 3 | 96 x 96 | 1 | 100 | 2000 | 500 | 0, 1 |

For the two AMU datasets, train with:

```sh
python IGI_PAEC_main_AMU_LSCC.py --run_mode train
python IGI_PAEC_main_AMU_CSCC.py --run_mode train
```

All three entry points default to `random_seed=1`, `num_workers=16`, and
`data_parallel=True`. The AMU scripts use their `*_WSI_with_PE` training and
test directories by default. Pass `--train_read_path`, `--test_read_path`,
`--val_read_path`, and the relevant output-path arguments to match your local
directory layout.

## :postbox: Contact
If you have any questions, please contact [Dr. Pan Huang](https://scholar.google.com/citations?user=V_7bX4QAAAAJ&hl=zh-CN) (`panhuang@polyu.edu.hk`).
