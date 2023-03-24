_base_ = [
    '../../resnet/resnet18_8xb16_cifar100.py'
]
# model settings
find_unused_parameters = False

# distillation settings
sd = True

# config settings
uskd = True

# method details
distiller = dict(
    type='ClassificationDistiller',
    teacher_pretrained = None,
    sd = sd,
    distill_cfg = [dict(methods=[dict(type='USKDLoss',
                                       name='loss_uskd',
                                       use_this = uskd,
                                       channel = 256,
                                       alpha=0.1,
                                       beta=0.1,
                                       mu=0.1,
                                       num_classes=100,
                                       )
                                ]
                        ),
                    ]
    )

student_cfg = 'configs/resnet/resnet18_8xb16_cifar100.py'
teacher_cfg = 'configs/resnet/resnet18_8xb16_cifar100.py'
