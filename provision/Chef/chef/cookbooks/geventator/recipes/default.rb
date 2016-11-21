include_recipe 'python'
include_recipe "python::pip"

package 'mongodb'
package 'python-setuptools'
package 'python-dev'
package 'python-pip'

python_pip 'Flask' do
  action :install
end

python_pip 'Flask-PyMongo' do
  action :install
end
