This template is meant to serve as a basic starting point for a deep learning project in PyTorch.
The template divides the implementation into 5 parts:
- `Model`: The deep learning architecture.
- `Data`: The DataLoader.
- `Loss`: The loss function used in training.
- `Optimizer`: The optimizer used for training.
- `Trainer`: The place where all 4 of the above come together to train your model.
You are encouraged to rename these classes, e.g. change `Model` to `UNet` or change `Loss` to `CrossEntropyLoss`.

Each class has an associated config object, which specifies all hyperparameters (e.g. `lr` for the learning rate in the `Optimizer`).

This template is intended to make it very simple to get a project started quickly.
There are superficial similarities to PyTorch Lightning, but the overall approach is different.
Rather than providing a new library at a higher level of abstraction, this template will create
a "pure" PyTorch project. This makes it easier to modify the components arbitrarily, and gets
rid of the need for learning new syntax.

The goal of this project is to approach some point on the "Pareto frontier" of automation: maximizing the amount of code which
is automatically generated, without sacrificing flexibility. Some ideas for achieving this goal are outlined in *FEATURE_IDEAS.MD*. 