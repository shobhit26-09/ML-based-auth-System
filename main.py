from utils.audio_utils import record_audio
from utils.data_utils import collect_data
from utils.model_utils import train_model, authenticate

if __name__ == "__main__":
    while True:
        print("Voice Authentication System")
        print("1. Collect Data")
        print("2. Train Model")
        print("3. Authenticate")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            collect_data()
        elif choice == '2':
            train_model()
        elif choice == '3':
            authenticate()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
