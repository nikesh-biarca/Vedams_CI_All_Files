for i in {4..20}
do
    #mkdir $i
    cd $i
    #git clone https://github.com/openstack-dev/ci-sandbox.git
    cd ci-sandbox/
    echo "hello_world = 128" >> test-1
    git add .
    #git config --global --add gitreview.username "nikem"
    #git commit -m "test" -a --amend
    git commit --amend -C HEAD
    git review
    cd
done
