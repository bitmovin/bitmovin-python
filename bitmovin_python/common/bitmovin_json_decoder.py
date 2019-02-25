import re
from enum import EnumMeta
from importlib import import_module

from bitmovin_python.models import PaginationResponse


class BitmovinJsonDecoder(object):
    model_module = import_module('bitmovin_python.models')

    @staticmethod
    def map_dict_to_pagination_response(result, model):
        model_to_return = BitmovinJsonDecoder.map_dict_to_model(result, PaginationResponse)

        pagination_items = list()

        model_instance = model()
        if 'discriminator_value_class_map' in model.__dict__:
            for i in model_to_return.items:
                discriminator_value = model_instance.discriminator_value_class_map[i['type']]
                pagination_items.append(
                    BitmovinJsonDecoder.map_dict_to_model(i,
                                                          getattr(BitmovinJsonDecoder.model_module,
                                                                  discriminator_value)))
        else:
            pagination_items = BitmovinJsonDecoder.map_dict_to_list(model_to_return.items, model)

        model_to_return.items = pagination_items
        return model_to_return

    @staticmethod
    def map_dict_to_list(result, model):
        list_to_return = list()
        for i in result:
            list_to_return.append(BitmovinJsonDecoder.map_dict_to_model(i, model))

        return list_to_return

    @staticmethod
    def map_dict_to_model(result, model):
        model_instance = model()
        all_attributes = model_instance.attribute_map
        for key in all_attributes:
            value = result.get(all_attributes.get(key))
            if value is not None:
                type = model_instance.openapi_types.get(key)
                try:

                    if re.match('list', type, re.I):
                        matches = re.search(r'\[(.*)\]', type)

                        if matches is not None and len(matches.groups()) is 1:
                            if getattr(BitmovinJsonDecoder.model_module, matches.group(1)):
                                model_class = getattr(BitmovinJsonDecoder.model_module,
                                                      matches.group(1))
                                new_value = list()
                                for k in value:
                                    val = k
                                    if isinstance(value, dict):
                                        val = value[k]

                                    new_value.append(
                                        BitmovinJsonDecoder.map_dict_to_model(val, model_class))
                                model_instance.__setattr__(key, new_value)
                                continue

                    model_class = getattr(BitmovinJsonDecoder.model_module, type)
                    if isinstance(model_class, EnumMeta):
                        # Search for the attribute in the Enum
                        for attr in model_class:
                            if attr.value == value:
                                value = attr
                                break

                        # Set the value
                        model_instance.__setattr__(key, value)
                        continue

                    new_value = BitmovinJsonDecoder.map_dict_to_model(value, model_class)
                    model_instance.__setattr__(key, new_value)
                except (NameError, AttributeError) as e:
                    # No model type that has to be special handled
                    if type == 'datetime':
                        from dateutil.parser import parse
                        new_value = parse(value)
                        model_instance.__setattr__(key, new_value)
                    else:
                        new_value = value
                        model_instance.__setattr__(key, new_value)
        return model_instance
