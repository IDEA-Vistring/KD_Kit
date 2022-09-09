_base_ = [
    '../../deit/deit-tiny_pt-4xb256_in1k.py'
]
# model settings
find_unused_parameters=True
use_logit = True
vitkd = True
wsld = False
dkd = False
kd = False
nkd = True
tf_nkd = False
distiller = dict(
    type='ClassificationDistiller',
    teacher_pretrained = 'https://download.openmmlab.com/mmclassification/v0/deit/deit-small_pt-4xb256_in1k_20220218-9425b9bb.pth',
    use_logit = use_logit,
    vitkd = vitkd,
    tf_nkd = tf_nkd,
    distill_cfg = [ dict(methods=[dict(type='ViTKDLoss',
                                       name='loss_vitkd',
                                       use_this = vitkd,
                                       student_dims = 192,
                                       teacher_dims = 384,
                                       alpha_vitkd=0.00003,
                                       beta_vitkd=0.000003,
                                       lambda_vitkd=0.5,
                                       )
                                ]
                        ),
                    dict(methods=[dict(type='WSLDLoss',
                                       name='loss_wsld',
                                       use_this = wsld,
                                       temp=2.0,
                                       alpha=2.5,
                                       num_classes=1000,
                                       )
                                ]
                        ),
                    dict(methods=[dict(type='DKDLoss',
                                       name='loss_dkd',
                                       use_this = dkd,
                                       temp=1.0,
                                       alpha=1.0,
                                       beta=0.5,
                                       )
                                ]
                        ),
                    dict(methods=[dict(type='NKDLoss',
                                       name='loss_nkd',
                                       use_this = nkd,
                                       temp=1.0,
                                       alpha=1.0,
                                       )
                                ]
                        ),
                    dict(methods=[dict(type='KDLoss',
                                       name='loss_kd',
                                       use_this = kd,
                                       temp=1.0,
                                       alpha=0.5,
                                       )
                                ]
                        ),

                   ]
    )

student_cfg = 'configs/deit/deit-tiny_pt-4xb256_in1k.py'
teacher_cfg = 'configs/deit/deit-small_pt-4xb256_in1k.py'
