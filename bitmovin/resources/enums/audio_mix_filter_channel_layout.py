import enum


class AudioMixFilterChannelLayout(enum.Enum):
    NONE = 'NONE'
    CL_MONO = 'MONO'
    CL_STEREO = 'STEREO'
    CL_2_1 = '2.1'
    CL_SURROUND = 'SURROUND'
    CL_3_1 = '3.1'
    CL_4_0 = '4.0'
    CL_4_1 = '4.1'
    CL_2_2 = '2.2'
    CL_QUAD = 'QUAD'
    CL_5_0 = '5.0'
    CL_5_1 = '5.1'
    CL_5_0_BACK = '5.0_BACK'
    CL_5_1_BACK = '5.1_BACK'
    CL_6_0 = '6.0'
    CL_6_0_FRONT = '6.0_FRONT'
    CL_HEXAGONAL = 'HEXAGONAL'
    CL_6_1 = '6.1'
    CL_6_1_BACK = '6.1_BACK'
    CL_6_1_FRONT = '6.1_FRONT'
    CL_7_0 = '7.0'
    CL_7_0_FRONT = '7.0_FRONT'
    CL_7_1 = '7.1'
    CL_7_1_WIDE = '7.1_WIDE'
    CL_7_1_WIDE_BACK = '7.1_WIDE_BACK'
    CL_OCTAGONAL = 'OCTAGONAL'
    CL_STEREO_DOWNMIX = 'STEREO_DOWNMIX'

    @staticmethod
    def default():
        return AudioMixFilterChannelLayout.NONE
