import ericAPIinterface

search='author:Kasumi Yamazaki'
records = ericAPIinterface.getAllERICRecords(search)
records.head()
records
