install:
	sudo apt-get install -y python-rdkit librdkit1 rdkit-data
	sudo apt-get install -y ipython ipython-notebook
	wget https://sites.google.com/site/pdynamomodeling/pDynamo-1.9.0.tgz
	tar xvzf pDynamo-1.9.0.tgz
	cd pDynamo-1.9.0 && python installation/Install.py
	rm -rf pDynamo-1.9.0.tgz
