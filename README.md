# image-2-text
![diagram](docs/online-ocr-diagram.png)
 Extract text from image using AWS Rekognition

This is an event driven component. An s3PutObject triggers the AWS Lambda that uses AWS Rekognition API to extract the texts from uploaded image on s3 bucket.

#### TO Do
* CI `circleci`
* Lambda POC          - `done`
* return all texts    - `done`
* Handle no text case - `done`

Find current version of a python library - `pip3 freeze | grep lib_name`

##### Ⓒ Ashraf Minhaj
##### Find me on LinkedIn [Ashraf-Minhaj](https://www.linkedin.com/in/ashraf-minhaj/)

#### Learn By Making.
#### Get your hands dirty to become a craftsman