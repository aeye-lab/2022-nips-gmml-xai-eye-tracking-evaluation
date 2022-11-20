repositories = {
    'gazebase_all_sr1000_sl1000': {
        'dirpath': 'data/gazebase_all_sr1000_sl1000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_all_sr1000_sl5000': {
        'dirpath': 'data/gazebase_all_sr1000_sl5000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_all_sr1000_sl10000': {
        'dirpath': 'data/gazebase_all_sr1000_sl10000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_task_all_sr1000_sl1000': {
        'dirpath': 'data/gazebase_all_sr1000_sl1000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_task_id.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_task_all_sr1000_sl5000': {
        'dirpath': 'data/gazebase_all_sr1000_sl5000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_task_id.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_task_all_sr1000_sl10000': {
        'dirpath': 'data/gazebase_all_sr1000_sl10000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_task_id.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_allnoblg_sr1000_sl1000': {
        'dirpath': 'data/gazebase_allnoblg_sr1000_sl1000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'gazebase_allnoblg_sr1000_sl5000': {
        'dirpath': 'data/gazebase_allnoblg_sr1000_sl5000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': [],
    },
    'judo_sr1000_sl1000': {
        'dirpath': 'data/judo_sr1000_sl1000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': ['saccade.npy', 'fixation.npy', 'corrupt.npy', 'none.npy'],
    },
    'mnist1d_sl1000': {
        'dirpath': 'data/mnist1d_sl1000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': ['pattern.npy'],
    },
    'mnist1d_sl1000_nonoise': {
        'dirpath': 'data/mnist1d_sl1000_nonoise/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        'event_filenames': ['pattern.csv'],
    },
    'potec_sr1000_sl1000': {
        'dirpath': 'data/potec_sr1000_sl1000/',
        'X': 'X.npy',
        'X_format': 'X_format.json',
        'Y': 'Y_cat.npy',
        'Y_labels': 'Y.npy',
        'Y_format': 'Y_format.json',
        'folds': 'folds.joblib',
        'label_encoder': 'label_encoder.joblib',
        'event_dirname': 'events',
        #'event_filenames': ['saccade.npy', 'fixation.npy', 'corrupt.npy', 'none.npy'],
        'event_filenames': [
            'mnh_fixation.npy',
            'mnh_noise.npy',
            'mnh_pso.npy',
            'mnh_saccade.npy',
            'mnh_unclassified.npy',

            'engbert_saccade.npy',
            'engbert_microsaccade.npy',
            'engbert_fixation.npy',
            'engbert_corrupt.npy',
            'engbert_none.npy',

        ],
    },
}
