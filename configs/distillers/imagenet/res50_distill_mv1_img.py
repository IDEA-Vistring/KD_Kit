_base_ = [
    '../../mobilenet_v1/mobilenet_v1.py'
]
# model settings
find_unused_parameters=True
use_logit = True
srrl = False
mgd = False
wsld = False
dkd = False
kd = False
nkd = True
tf_nkd = False
distiller = dict(
    type='ClassificationDistiller',
    teacher_pretrained = 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb32_in1k_20210831-ea4938fc.pth',
    use_logit = use_logit,
    tf_nkd = tf_nkd,
    distill_cfg = [ dict(methods=[dict(type='SRRLLoss',
                                       name='loss_srrl',
                                       use_this = srrl,
                                       student_channels = 1024,
                                       teacher_channels = 2048,
                                       alpha=1.0,
                                       beta=1.0,
                                       )
                                ]
                        ),
                    dict(methods=[dict(type='MGDLoss',
                                       name='loss_mgd',
                                       use_this = mgd,
                                       student_channels = 1024,
                                       teacher_channels = 2048,
                                       alpha_mgd=0.00007,
                                       lambda_mgd=0.15,
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
                                       alpha=1.5,
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

student_cfg = 'configs/mobilenet_v1/mobilenet_v1.py'
teacher_cfg = 'configs/resnet/resnet50_b32x8_imagenet.py'
optimizer_config = dict(_delete_=True,grad_clip=dict(max_norm=5.0))