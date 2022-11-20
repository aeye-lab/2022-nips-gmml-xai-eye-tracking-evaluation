import numpy as np
import quantus


metrics = {
    # pixelflipping mean
    'pixel_flipping_mean_abs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'morf',
            'perturb_baseline': 'mean',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_mean_noabs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'morf',
            'perturb_baseline': 'mean',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_mean_abs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'lerf',
            'perturb_baseline': 'mean',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_mean_noabs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'lerf',
            'perturb_baseline': 'mean',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_mean_noabs_nonorm_random': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'random',
            'perturb_baseline': 'mean',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },

    # pixelflipping uniform
    'pixel_flipping_uniform_abs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'morf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'prediction_difference': True,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_uniform_noabs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'morf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'prediction_difference': True,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_uniform_abs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'lerf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'prediction_difference': True,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_uniform_noabs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'lerf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'prediction_difference': True,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_uniform_noabs_nonorm_random': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'random',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'prediction_difference': True,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },

    # pixelflipping gaussian
    'pixel_flipping_gaussian_abs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'morf',
            'perturb_baseline': 'gaussian',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_gaussian_noabs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'morf',
            'perturb_baseline': 'gaussian',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_gaussian_abs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'lerf',
            'perturb_baseline': 'gaussian',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_gaussian_noabs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'lerf',
            'perturb_baseline': 'gaussian',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_gaussian_noabs_nonorm_random': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'random',
            'perturb_baseline': 'gaussian',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },

    # pixelflipping saltnpepper
    'pixel_flipping_saltnpepper_abs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'morf',
            'perturb_baseline': 'saltnpepper',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_saltnpepper_noabs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'morf',
            'perturb_baseline': 'saltnpepper',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_saltnpepper_abs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'lerf',
            'perturb_baseline': 'saltnpepper',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_saltnpepper_noabs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'lerf',
            'perturb_baseline': 'saltnpepper',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'pixel_flipping_saltnpepper_noabs_nonorm_random': {
        'framework': 'quantus',
        'class': quantus.PixelFlipping,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'random',
            'perturb_baseline': 'saltnpepper',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'features_in_step': 2,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },

    # region perturbation uniform size=3
    'region_perturbation_s3_uniform_abs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'morf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 3,
            'n_steps': 100,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s3_uniform_noabs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'morf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 3,
            'n_steps': 334,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s3_uniform_abs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'lerf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 3,
            'n_steps': 100,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s3_uniform_noabs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'lerf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 3,
            'n_steps': 100,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s3_uniform_noabs_nonorm_random': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'random',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 3,
            'n_steps': 334,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },


    # region perturbation uniform size=5
    'region_perturbation_s5_uniform_abs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'morf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 5,
            'n_steps': 100,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s5_uniform_noabs_nonorm_morf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'morf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 5,
            'n_steps': 400,
            'regions_per_step': 1,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s5_uniform_abs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'order': 'lerf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 5,
            'n_steps': 100,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s5_uniform_noabs_nonorm_lerf': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'lerf',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 5,
            'n_steps': 100,
            'regions_per_step': '$dataset_factor',
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'region_perturbation_s5_uniform_noabs_nonorm_random': {
        'framework': 'quantus',
        'class': quantus.RegionPerturbation,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'order': 'random',
            'perturb_baseline': 'uniform',
            'perturb_func': quantus.baseline_replacement_by_indices,
            'patch_size': 5,
            'n_steps': 400,
            'regions_per_step': 1,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },




    'pointing_game': {
        'framework': 'quantus',
        'class': quantus.PointingGame,
        'init_kwargs': {
            'weighted': False,
            'normalise': False,
            'abs': False,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'pointing_game_weighted': {
        'framework': 'quantus',
        'class': quantus.PointingGame,
        'init_kwargs': {
            'weighted': True,
            'normalise': False,
            'abs': False,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'attribution_localisation': {
        'framework': 'quantus',
        'class': quantus.AttributionLocalisation,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'weighted': False,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'attribution_localisation_weighted': {
        'framework': 'quantus',
        'class': quantus.AttributionLocalisation,
        'init_kwargs': {
            'normalise': False,
            'abs': True,
            'weighted': True,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_10_intersection': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'k': 10,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_25_intersection': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'k': 25,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_50_intersection': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'k': 50,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_100_intersection': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'k': 100,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_10_intersection_concept_influence': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'concept_influence': True,
            'normalise': False,
            'abs': False,
            'k': 10,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_25_intersection_concept_influence': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'concept_influence': True,
            'normalise': False,
            'abs': False,
            'k': 25,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_50_intersection_concept_influence': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'concept_influence': True,
            'normalise': False,
            'abs': False,
            'k': 50,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'top_100_intersection_concept_influence': {
        'framework': 'quantus',
        'class': quantus.TopKIntersection,
        'init_kwargs': {
            'concept_influence': True,
            'normalise': False,
            'abs': False,
            'k': 100,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'relevance_rank_accuracy': {
        'framework': 'quantus',
        'class': quantus.RelevanceRankAccuracy,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'relevance_mass_accuracy': {
        'framework': 'quantus',
        'class': quantus.RelevanceMassAccuracy,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },
    'area_under_curve': {
        'framework': 'quantus',
        'class': quantus.AUC,
        'init_kwargs': {
            'normalise': False,
            'abs': False,
            'disable_warnings': True,
            'display_progressbar': False,
        },
        'call_kwargs': {},
    },

    # AXIOMATIC METRICS

    'completeness': {
        'framework': 'quantus',
        'class': quantus.Completeness,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'nonsensitivity': {
        'framework': 'quantus',
        'class': quantus.NonSensitivity,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'input_invariance': {
        'framework': 'quantus',
        'class': quantus.InputInvariance,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
            'input_shift': -1,
        },
        'call_kwargs': {},
    },

    # COMPLEXITIY METRICS

    'sparseness': {
        'framework': 'quantus',
        'class': quantus.Sparseness,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'entropy': {
        'framework': 'quantus',
        'class': quantus.Complexity,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'effective_complexity': {
        'framework': 'quantus',
        'class': quantus.EffectiveComplexity,
        'init_kwargs': {
            'eps': np.geomspace(1e-10, 1, num=1000),
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },

    # RANDOMISATION METRICS

    'model_parameter_randomisation': {
        'framework': 'quantus',
        'class': quantus.ModelParameterRandomisation,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },
    'random_logit': {
        'framework': 'quantus',
        'class': quantus.RandomLogit,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {},
    },

    # ROBUSTNESS METRICS

    'local_lipschitz_estimate': {
        'framework': 'quantus',
        'class': quantus.LocalLipschitzEstimate,
        'init_kwargs': {
            'nr_samples': 100,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'max_sensitivity': {
        'framework': 'quantus',
        'class': quantus.MaxSensitivity,
        'init_kwargs': {
            'nr_samples': 100,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'max_sensitivity_gaussian': {
        'framework': 'quantus',
        'class': quantus.MaxSensitivity,
        'init_kwargs': {
            'nr_samples': 100,
            'perturb_func': quantus.helpers.perturb_func.gaussian_noise,
            'perturb_func_kwargs': {
                'perturb_mean': 0.0,
                'perturb_std': 0.1,
            },
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'avg_sesitivity': {
        'framework': 'quantus',
        'class': quantus.MaxSensitivity,
        'init_kwargs': {
            'nr_samples': 100,
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },
    'continuity': {
        'framework': 'quantus',
        'class': quantus.Continuity,
        'init_kwargs': {
            'disable_warnings': True,
            'display_progressbar': True,
        },
        'call_kwargs': {
            'target': 'predicted',
        },
    },

    'accuracy': {
    },
}