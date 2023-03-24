# SGLD in PyTorch

[![PyPI version](https://badge.fury.io/py/torch-sgld.svg)](https://pypi.org/project/torch-sgld/)

This package implements [SGLD](https://icml.cc/2011/papers/398_icmlpaper.pdf) 
and [cSGLD](https://arxiv.org/abs/1902.03932)
as a [PyTorch Optimizer](https://pytorch.org/docs/stable/optim.html).

## Installation

Install from `pip` as:
```shell
pip install torch-sgld
```

To install the latest directly from source, run
```shell
pip install git+https://github.com/activatedgeek/torch-sgld.git
```

## Usage

The general idea is to modify the usual gradient-based update loops
in PyTorch with the `SGLD` optimizer.

```python
from torch_sgld import SGLD

f = module()  ## construct PyTorch nn.Module.

sgld = SGLD(f.parameters(), lr=lr, momentum=.9)  ## Add momentum to make it SG-HMC.
sgld_scheduler = ## Optionally add a step-size scheduler.

for _ in range(num_steps):
    energy = f()
    energy.backward()

    sgld.step()

    sgld_scheduler.step()  ## Optional scheduler step.
```

`cSGLD` can be implemented by using a cyclical learning rate schedule.
See the [toy_csgld.ipynb](./notebooks/toy_csgld.ipynb) notebook for a
complete example.

## License

Apache 2.0