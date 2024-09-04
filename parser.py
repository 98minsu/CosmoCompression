import optuna
import sqlite3

def fetch_default_study_name(db_path):
    """ Fetch the default or only study name from the Optuna database. """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("SELECT study_name FROM studies;")
    study_names = cursor.fetchall()
    connection.close()
    # Assuming there's only one study per database or we take the first one
   # print (study_names)
    return study_names[0][0] #if study_names else None

def print_best_study_results(key, p):
    """ Print the best parameters and validation loss for a specific study. """
    # Formulate the storage URL and path based on key and p
    db_path = f'/pscratch/sd/m/minsu98/optuna/{key}_{p}.db'
    storage_url = f'sqlite:///{db_path}'
    
    if 1==1:
    #try:
        # Fetch the study name if needed or assume it's the default unnamed study
        study_name = fetch_default_study_name(db_path) or "default_study"  # Use a placeholder if none is found
        
        # Load the existing Optuna study
        study = optuna.load_study(study_name=study_name, storage=storage_url)
        best_trial = study.best_trial
        latest_trial = max(study.trials, key=lambda t: t.number)  # Find the trial with the highest number

        total_trials = len(study.trials)
        completed_trials = sum(1 for trial in study.trials if trial.state == optuna.trial.TrialState.COMPLETE)
        running_trials = sum(1 for trial in study.trials if trial.state == optuna.trial.TrialState.RUNNING)
        failed_trials = sum(1 for trial in study.trials if trial.state == optuna.trial.TrialState.FAIL)
        waiting_trials = sum(1 for trial in study.trials if trial.state == optuna.trial.TrialState.WAITING)

        print(f'Total trials for {key}_{p}: {total_trials}')
        print(f'  Completed: {completed_trials}')
        print(f'  Running: {running_trials}')
        #exact_trials(f'  Failed: {failed_trials}')
        print(f'  Waiting: {waiting_trials}')
        
        if completed_trials > 0:
            print(f'Best parameters for {key}_{p}:', best_trial.params)
            print(f'Best validation loss for {key}_{p}:', best_trial.value)
            print(f'Trial ID for the best result: {best_trial.number}')  # Print the trial number
            print(f'Latest trial ID: {latest_trial.number}')  # Print the latest trial number

    #except Exception as e:
    #    print(f"Error loading or analyzing the study for {key}_{p}: {e}")

def main():
    # Example keys and parameter indices
    keys = ['WL_2', 'WL_23_WPH_short_CMBWL']
    parameters = range(16)

    # Iterate through combinations or select specific ones
    for key in keys:
        print (key)
        for p in parameters:
            try:
                print_best_study_results(key, p)
            except:
                pass
        print ('')

if __name__ == '__main__':
    main()
