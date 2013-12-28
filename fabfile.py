from fabric.api import local, prompt


def determine_refspec_to_deploy_from(is_test=False):
    local('git fetch --tags')

    if is_test:
        create_tag = prompt('Tag this release? [y/N] ')
        if create_tag.lower() == 'y':
            print("Showing latest tags for reference")
            local('git tag | sort -V | tail -5')
            refspec = prompt('Tag name [in format x.x.x]? ')
            local('git tag %(ref)s -m "Tagging version %(ref)s in fabfile"' % {
                'ref': refspec})
            local('git push --tags')
        else:
            use_commit = prompt('Build from a specific commit? [y/N] ')
            if use_commit.lower() == 'y':
                refspec = prompt('Choose commit to build from: ')
            else:
                branch = local('git branch | grep "^*" | cut -d" " -f2',
                capture=True)
                refspec = local('git describe %s' % branch,
                     capture=True).strip()
    else:
        # An existing tag must be specified
        local('git tag | sort -V | tail -5')
        refspec = prompt('Choose tag to build from: ')

        # Check this is valid
        local('git tag | grep "%s"' % refspec)

    return refspec


def prepare_deploy():
    local('git add .')
    print("enter your git commit comment: ")
    comment = raw_input()
    local('git commit -m "%s"' % comment)
    local('git push -u origin master')


def deploy():
    local('heroku maintenance:on')
    local('git push heroku master')
    local('heroku maintenance:off')
