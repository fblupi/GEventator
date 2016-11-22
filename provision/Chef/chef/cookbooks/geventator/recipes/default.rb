apt_update 'all platforms'

package 'mongodb'
package 'python-setuptools'
package 'python-dev'
package 'python-pip'

easy_install_package 'Flask'
easy_install_package 'Flask-PyMongo'
