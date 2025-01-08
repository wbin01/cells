#!/bin/bash
echo "Cells:"
time bash -c "python demo.py & sleep 2; pkill python"
echo
echo "------"
echo "Pyside:"
time bash -c "python test.py & sleep 2; pkill python"
