from bitmovin.utils import Serializable


class BroadcastTsProgramConfiguration(Serializable):

    def __init__(self, program_number=None, pid_for_pmt=None, insert_program_clock_ref_on_pes=None):
        super().__init__()
        self.programNumber = program_number
        self.pidForPMT = pid_for_pmt
        self.insertProgramClockRefOnPes = insert_program_clock_ref_on_pes

    @classmethod
    def parse_from_json_object(cls, json_object):
        program_number = json_object.get('programNumber')
        pid_for_pmt = json_object.get('pidForPMT')
        insert_program_clock_ref_on_pes = json_object.get('insertProgramClockRefOnPes')

        return BroadcastTsProgramConfiguration(program_number=program_number, pid_for_pmt=pid_for_pmt,
                                               insert_program_clock_ref_on_pes=insert_program_clock_ref_on_pes)
