# === IMPORTS: BUILT-IN ===
import os

# === IMPORTS: THIRD-PARTY ===
from tqdm import trange
import torch

# === IMPORTS: LOCAL ===
from src.configs.configs import TrainerConfig, OptimizerConfig, ModelConfig, LossConfig, DataConfig
from src.loss import Loss
from src.model import Model
from src.data_manager import DataManager
from src.optimizer import Optimizer


class Trainer:
    def __init__(
        self, 
        training_config: TrainerConfig,
        optimizer_config: OptimizerConfig,
        model_config: ModelConfig,
        loss_config: LossConfig,
        data_config: DataConfig
    ):
        self.training_config = training_config
        self.optimizer_config = optimizer_config
        self.model_config = model_config
        self.loss_config = loss_config
        self.data_config = data_config

    def get_dataloader(self):
        data_manager = DataManager(self.data_config)
        return data_manager.get_data()

    def get_model(self):
        model = Model(self.model_config)
        return model

    def get_optimizer(self, model: Model):
        oc = self.optimizer_config
        optimizer = Optimizer(oc).get_optimizer(model)
        return optimizer
    
    def get_loss(self):
        loss_function = Loss(self.loss_config)
        return loss_function

    def train(self):
        c = self.training_config

        dataloader = self.get_dataloader()
        model = self.get_model()
        optimizer = self.get_optimizer(model)
        loss_function = self.get_loss()

        for epoch in trange(c.num_epochs):
            for data in trange(dataloader):
                # TODO: Implement the steps for a forward pass
                prediction = model(data)
                loss = loss_function(prediction, data)

                # === BACKPROPAGATION ===
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            torch.save(model.state_dict(), os.path.join("models", c.folder, f"ckpt.pt"))