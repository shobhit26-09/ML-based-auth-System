import os
import numpy as np
from utils.audio_utils import record_audio, augment_audio
from utils.feature_utils import extract_features

DATA_DIR = "data/voice_samples"

def collect_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    user_id = input("Enter user ID: ")
    user_dir = os.path.join(DATA_DIR, user_id)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    existing_samples = len([name for name in os.listdir(user_dir) if name.endswith(".npy")])
    for i in range(existing_samples, existing_samples + 5):
        print(f"Recording sample {i + 1} for user {user_id}")
        audio = record_audio()
        augmented_audios = augment_audio(audio)
        for j, aug_audio in enumerate(augmented_audios):
            features = extract_features(aug_audio)
            np.save(os.path.join(user_dir, f"sample_{i + 1}_{j}.npy"), features)
    print(f"Data collection for user {user_id} complete")
