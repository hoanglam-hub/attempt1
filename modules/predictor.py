import numpy as np
import torch
import torch.nn as nn

class DrowsinessLSTM(nn.Module):

    def __init__(self, input_size=5, hidden_size=32, num_layers=1):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )
        self.fc = nn.Sequential(
            nn.Linear(hidden_size, 16),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(16, 1)
        )

    def forward(self, x):
        out, _ = self.lstm(x)
        out = out[:, -1, :]
        out = self.fc(out)

        return out

class Predictor:
    def __init__(self, model_path, mean_path, std_path, device):
        self.model = DrowsinessLSTM()
        self.model.load_state_dict(torch.load(model_path, map_location=device))
        self.model.eval()
        self.mean = np.load(mean_path)
        self.std = np.load(std_path)

    def predict(self, input):
        input = (input - self.mean) / self.std
        input = torch.tensor(input, dtype=torch.float32).unsqueeze(0)

        with torch.inference_mode():
            output = torch.sigmoid(self.model(input)).item()
        return output

