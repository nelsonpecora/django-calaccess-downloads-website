# Fix the locale
execute "create-locale" do
  command %Q{
    locale-gen en_US.UTF-8
  }
end

execute "set-locale" do
  command %Q{
    update-locale LANG=en_US.UTF-8
  }
end

# Load any base system wide packages
node[:base_packages].each do |pkg|
    package pkg do
        :upgrade
    end
end

# Loop through the user list, create the user, load the authorized_keys
# and mint a bash_profile
node[:users].each_pair do |username, info|

    group username do
       gid info[:id] 
    end

    user username do 
        comment info[:full_name]
        uid info[:id]
        gid info[:id]
        shell info[:disabled] ? "/sbin/nologin" : "/bin/bash"
        supports :manage_home => true
        home "/home/#{username}"
    end

    template "/home/#{username}/.bash_profile" do
        source "users/bash_profile.erb"
        owner username
        group username
        mode 0755
        variables({
          :aws_access_key_id => node[:aws_access_key_id],
          :aws_secret_access_key => node[:aws_secret_access_key],
          :db_host => node[:db_host],
          :db_password => node[:db_user_password]
        })
    end
end

# Set the user groups
node[:groups].each_pair do |name, info|
    group name do
        gid info[:gid]
        members info[:members]
    end
end

template "/etc/sudoers" do
  source "users/sudoers.erb"
  mode 0440
  owner "root"
  group "root"
  variables({
     :apps_user => node[:apps_user]
  })
end

