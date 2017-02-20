all:
	protoc --python_out=. ./test.proto
	python generate-api-rc.py 
clean:
	rm -f *.pyc
	rm -f apirc.*
	rm -f *_pb2.py
