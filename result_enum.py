from enum import Enum

Project = ['文件名', '人脸置信度', '性别', '性别概率', '年龄',
           '种族', '种族概率', '表情', '表情概率', '脸型',
           '脸型概率','真实、卡通人脸', '概率', '情绪', '情绪概率',
           'YAW','PITCH','RAW','角度','左眼遮挡',
           '右眼遮挡', '鼻子遮挡', '嘴遮挡','左脸遮挡','左脸遮挡',
           '下巴遮挡', '遮挡', '模糊度','光照度', '完整度',
           '眼镜类型', '眼镜概率','左眼睁开', '右眼睁开']

class ResultEnum(Enum):
    NAME           = 1
    PROBABILITY    = 2
    GENDER         = 3
    GENDERRATE     = 4
    AGE            = 5
    RACE           = 6
    RACERATE       = 7
    EXPRESSION     = 8
    EXPRESSIONRATE = 9
    FACESHARP      = 10
    FACESHARPRATE  = 11
    FACETYPE       = 12
    FACETYPERATE   = 13
    FACEEMOTION    = 14
    FACEEMOTIONRATE= 15
    YAW            = 16
    PITCH          = 17
    ROLL           = 18
    ANGLEOK        = 19
    LEFTEYE        = 20
    RIGHTEYE       = 21
    NOSE           = 22
    MOUTH          = 23
    LEFTCHEEK      = 24
    RIGHTCHEEK     = 25
    CHIN           = 26
    SHAOW          = 27
    BLUR           = 28
    ILLUMINATION   = 29
    COMPLETENESS   = 30
    GLASSTYPE      = 31
    GLASSRATE      = 32
    LEFTEYEOPEN    = 33
    RIGHTEYEOPEN   = 34
