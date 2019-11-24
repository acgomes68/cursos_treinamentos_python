docker run -it continuumio/anaconda3:2019.10-alpine /bin/sh

docker run -i -t -p 8888:8888 continuumio/anaconda3:2019.10-alpine /bin/sh -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"

http://127.0.0.1:8888/?token=f32b6f204ccc1b40ae740a0808493a3bf8cbd6356f55eb35
