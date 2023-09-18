
import pandas as pd
import json

class Generic:

    def __init__(self, record: dict):
        for k, v in record.items():
            setattr(self, k, v)

    @staticmethod
    def dict_to_object(data: dict, ctx):
        print(data, ctx)
        return Generic(record=data)


    def to_dict(self):
        return self.__dict__

    @classmethod
    def get_object(cls, file_path):
        chunk_df = pd.read_csv(file_path, chunksize=10)
        n_row = 0
        for df in chunk_df:
            for data in df.values:
                generic = Generic(dict(zip(df.columns, list(map(str,data)))))
                # cars.append(car)
                # print(n_row)
                n_row += 1
                yield generic


   
    @classmethod
    def export_schema_to_create_confluent_schema(cls, file_path):    
        columns = next(pd.read_csv(file_path, chunksize=10)).columns

        schema = dict()
        schema.update({
                    "type": "record",
                    "namespace": "com.mycorp.mynamespace",
                    "name": "sampleRecord",
                    "doc": "Sample schema to help you get started.",
                    })

        fields = []    
        for column in columns:
            fields.append(
                        {
                        "name": f"{column}",
                        "type": "string",
                        "doc": "The string type."  
                        }
            )

        schema.update({"fields":fields})


    
        json.dump(schema,open("schema.json","w"))
        schema = json.dumps(schema)

        print(schema)
        return schema
        

   # export_schema_to_create_confluent_schema  to generate json formate  by taking the file  .csv
   # using pandas we are readinfg the csv file in that we are passing the csv file and  chunksize=10
   # chunksize= 10 --> if .csv file is may rows and colume it will take time  for analysing we are taking simpley 10 records  if you read more GB it will system will cresh

    @classmethod
    def get_schema_to_produce_consume_data(cls, file_path):
        columns = next(pd.read_csv(file_path, chunksize=10)).columns

        schema = dict()  # creating dict
        schema.update({
            "$id": "http://example.com/myURI.schema.json",    # url for reference 
            "$schema": "http://json-schema.org/draft-07/schema#",  # url for reference 
            "additionalProperties": False,
            "description": "Sample schema to help you get started.",
            "properties": dict(), # creating dict
            "title": "SampleRecord",
            "type": "object"})   # in schema dict we are storing in the form of object type 
        for column in columns:    # columns are defined in top 
            schema["properties"].update(
                {
                    # in reality we need to take care  depends on each and every IOT  data Based on that we need to write a code  type also need to change
                    f"{column}": {  # columan
                        "description": f"generic {column} ", #column descreption 
                        "type": "string"   #every colum as a string 
                    }
                }
            )
        
    
        schema = json.dumps(schema)

        print(schema)
        return schema
        

    def __str__(self):
        return f"{self.__dict__}"


def instance_to_dict(instance: Generic, ctx):
    return instance.to_dict()
