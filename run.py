# encoding: utf-8
import os
from os.path import join

xml_path = "/xml_path"
xsl_path = "/xsl_path/transformer.xsl"
output_path = "/output_path"
counter = 1
for workdir, dirs, files in os.walk(xml_path):
    for name in files:
        # prepare input file name
        full_input_file = join(workdir, name)

        # prepare output file name with json extension
        full_output_file = join(output_path, name)
        pre, ext = os.path.splitext(full_output_file)
        full_output_file = pre + '.json'

        # if not xml, skip the current file
        if not full_input_file.endswith('xml'):
            continue

        print(f'### {counter} reading {full_input_file}')
        counter += 1
        os.system(f"saxonb-xslt -o {full_output_file} -s {full_input_file} -xsl {xsl_path}")
