from bitmovin.resources.enums import ChromaLocation, ColorSpace, ColorPrimaries, ColorRange, InputColorSpace, \
    InputColorRange, ColorTransfer
from bitmovin.errors import InvalidTypeError
from bitmovin.utils import Serializable


class ColorConfig(Serializable):
    def __init__(self, copy_chroma_location_flag=None, copy_color_space_flag=None, copy_color_primaries_flag=None,
                 copy_color_range_flag=None, copy_color_transfer_flag=None, chroma_location=None, color_space=None,
                 color_primaries=None, color_range=None, color_transfer=None, input_color_space=None,
                 input_color_range=None):
        super().__init__()

        self._chromaLocation = None
        self._colorSpace = None
        self._colorPrimaries = None
        self._colorRange = None
        self._colorTransfer = None
        self._inputColorSpace = None
        self._inputColorRange = None

        self.copyChromaLocationFlag = copy_chroma_location_flag
        self.copyColorSpaceFlag = copy_color_space_flag
        self.copyColorPrimariesFlag = copy_color_primaries_flag
        self.copyColorRangeFlag = copy_color_range_flag
        self.copyColorTransferFlag = copy_color_transfer_flag
        self.chromaLocation = chroma_location
        self.colorSpace = color_space
        self.colorPrimaries = color_primaries
        self.colorRange = color_range
        self.colorTransfer = color_transfer
        self.inputColorSpace = input_color_space
        self.inputColorRange = input_color_range

    @property
    def chromaLocation(self):
        return self._chromaLocation

    @chromaLocation.setter
    def chromaLocation(self, new_chroma_location):
        if new_chroma_location is None:
            return
        elif isinstance(new_chroma_location, str):
            self._chromaLocation = new_chroma_location
        elif isinstance(new_chroma_location, ChromaLocation):
            self._chromaLocation = new_chroma_location.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of chromaLocation. It has to be of type ChromaLocation or str'.format(
                    type(new_chroma_location)
                ))

    @property
    def colorSpace(self):
        return self._colorSpace

    @colorSpace.setter
    def colorSpace(self, new_color_space):
        if new_color_space is None:
            return
        elif isinstance(new_color_space, str):
            self._colorSpace = new_color_space
        elif isinstance(new_color_space, ColorSpace):
            self._colorSpace = new_color_space.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of colorSpace. It has to be of type ColorSpace enum or str'.format(
                    type(new_color_space)
                ))


    @property
    def colorPrimaries(self):
        return self._colorPrimaries

    @colorPrimaries.setter
    def colorPrimaries(self, new_color_primaries):
        if new_color_primaries is None:
            return
        elif isinstance(new_color_primaries, str):
            self._colorPrimaries = new_color_primaries
        elif isinstance(new_color_primaries, ColorPrimaries):
            self._colorPrimaries = new_color_primaries.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of colorPrimaries. It has to be of type ColorPrimaries enum or str'.format(
                    type(new_color_primaries)
                ))

    @property
    def colorRange(self):
        return self._colorRange

    @colorRange.setter
    def colorRange(self, new_color_range):
        if new_color_range is None:
            return
        elif isinstance(new_color_range, str):
            self._colorRange = new_color_range
        elif isinstance(new_color_range, ColorRange):
            self._colorRange = new_color_range.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of colorRange. It has to be of type ColorRange enum or str'.format(
                    type(new_color_range)
                ))

    @property
    def colorTransfer(self):
        return self._colorTransfer

    @colorTransfer.setter
    def colorTransfer(self, new_color_transfer):
        if new_color_transfer is None:
            return
        elif isinstance(new_color_transfer, str):
            self._colorTransfer = new_color_transfer
        elif isinstance(new_color_transfer, ColorTransfer):
            self._colorTransfer = new_color_transfer.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of colorTransfer. It has to be of type ColorTransfer enum or str'.format(
                    type(new_color_transfer)
                ))

    @property
    def inputColorSpace(self):
        return self._inputColorSpace

    @inputColorSpace.setter
    def inputColorSpace(self, new_input_color_space):
        if new_input_color_space is None:
            return
        elif isinstance(new_input_color_space, str):
            self._inputColorSpace = new_input_color_space
        elif isinstance(new_input_color_space, InputColorSpace):
            self._inputColorSpace = new_input_color_space.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of inputColorSpace. It has to be of type InputColorSpace enum or str'.format(
                    type(new_input_color_space)
                ))

    @property
    def inputColorRange(self):
        return self._inputColorRange

    @inputColorRange.setter
    def inputColorRange(self, new_input_color_range):
        if new_input_color_range is None:
            return
        elif isinstance(new_input_color_range, str):
            self._inputColorRange = new_input_color_range
        elif isinstance(new_input_color_range, InputColorRange):
            self._inputColorRange = new_input_color_range.value
        else:
            raise InvalidTypeError(
                'Invalid type {} of inputColorRange. It has to be of type InputColorRange enum or str'.format(
                    type(new_input_color_range)
                ))

    def serialize(self):
        serialized = super().serialize()
        serialized['chromaLocation'] = self.chromaLocation
        serialized['colorSpace'] = self.colorSpace
        serialized['colorPrimaries'] = self.colorPrimaries
        serialized['colorRange'] = self.colorRange
        serialized['colorTransfer'] = self.colorTransfer
        serialized['inputColorSpace'] = self.inputColorSpace
        serialized['inputColorRange'] = self.inputColorRange

        return serialized
