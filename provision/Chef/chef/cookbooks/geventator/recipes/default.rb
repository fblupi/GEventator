apt_update 'all platforms'

package 'mongodb'
package 'python-setuptools'
package 'python-dev'
package 'python-pip'

execute 'Flask' do
  command 'pip install Flask'
end

execute 'Flask-PyMongo' do
  command 'pip install Flask-PyMongo'
end
