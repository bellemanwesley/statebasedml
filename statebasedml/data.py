from copy import copy

def train(datadict,*args, **kwargs):
    model = kwargs.get('model', {})
    for key in datadict:
        keydata = datadict[key]
        if "options" in keydata:
            assert type(keydata["options"]) == list, "options parameter must be list"
            assert "choice" in keydata, "Must have choice parameter if you have options parameter"
            assert keydata["choice"] in keydata["options"], "Choice parameter must be item in options parameter"
            if key in model:
                assert model[key]["options"] == True, "All keys with the same value must share options settings"
        if key in model:
            update_key = copy(model[key])
        else:
            if "options" in keydata:
                update_key = {"option_dict":{}}
            else:
                update_key = {"count":0,"result_dict":{}}
        if "option_dict" in update_key:
            for x in keydata["options"]:
                if x not in update_key["option_dict"]:
                    update_key["option_dict"].update({
                        x:{
                            "count":0,
                            "result_dict": {}
                        }
                    })
            if keydata["result"] not in update_key["option_dict"][keydata["choice"]]["result_dict"]:
                update_key["option_dict"][keydata["choice"]]["result_dict"].update(
                    {keydata["result"]:0}
                )
            update_key["option_dict"][keydata["choice"]]["count"] += 1
            update_key["option_dict"][keydata["choice"]]["result_dict"][keydata["result"]] += 1
        if "result_dict" in update_key:
            if keydata["result"] not in update_key["result_dict"]:
                update_key["result_dict"].update(
                    {keydata["result"]:0}
                )
            update_key["count"] += 1
            update_key["result_dict"][keydata["result"]] += 1                
        model.update({key:update_key})
    return model

def update(datadict,model):
    return train(datadict,model)

def classify(datadict,model):
    classifications = {}
    for key in datadict:
        if "option_dict" in datadict[key]:
