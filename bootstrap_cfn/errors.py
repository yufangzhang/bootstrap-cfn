import sys


class BootstrapCfnError(Exception):
    def __init__(self, msg):
        super(BootstrapCfnError, self).__init__(msg)
        print >> sys.stderr, "[ERROR] {0}: {1}".format(self.__class__.__name__, msg)


class CfnConfigError(BootstrapCfnError):
    pass


class CfnTimeoutError(BootstrapCfnError):
    pass


class CfnHostnamePatternError(BootstrapCfnError):
    pass


class NoCredentialsError(BootstrapCfnError):
    def __init__(self):
        super(NoCredentialsError, self).__init__(
            "Create an ~/.aws/credentials file by following this layout:\n\n" +
            "  http://boto.readthedocs.org/en/latest/boto_config_tut.html#credentials"
        )


class ProfileNotFoundError(BootstrapCfnError):
    def __init__(self, profile_name):
        super(ProfileNotFoundError, self).__init__(
            "'{0}' not found in ~/.aws/credentials".format(profile_name)
        )


class ZoneIDNotFoundError(BootstrapCfnError):
    def __init__(self, zone_name):
        msg = ("Could not find a zone id for zone name '{}'."
               "Please check that this hosted zone exists "
               "and is in the account you've specified".format(zone_name))
        super(ZoneIDNotFoundError, self).__init__(msg)


class ZoneRoute53RecordNotFoundError(BootstrapCfnError):
    def __init__(self, zone_name, zone_id):
        msg = ("Could not find an AWS Route53 record for zone name '{}' with zone id '{}'. "
               "Please check that this record exists in the account you've specified".format(zone_name, zone_id))
        super(ZoneRoute53RecordNotFoundError, self).__init__(msg)


class DNSRecordNotFoundError(BootstrapCfnError):
    def __init__(self, zone_name):
        msg = ("Could not find a dns record for zone name '{}'. "
               "Please check that this record exists".format(zone_name))
        super(DNSRecordNotFoundError, self).__init__(msg)


class CloudResourceNotFoundError(BootstrapCfnError):
    pass


class OSTypeNotFoundError(BootstrapCfnError):
    def __init__(self, type, available_types):
        msg = ("The os type '{}' is not recognised, should be one of {}. "
               .format(type, available_types))
        super(OSTypeNotFoundError, self).__init__(msg)


class AutoscalingGroupNotFound(BootstrapCfnError):
    pass


class AutoscalingInstanceCountError(BootstrapCfnError):
    def __init__(self, autoscaling_group, expected_instance_count, instances):
        super(AutoscalingInstanceCountError, self).__init__(
            "Could not find {} instances in autoscaling group {}. Actual state is {} instances, {}"
            .format(expected_instance_count, autoscaling_group, len(instances), instances)
        )


class TagRecordExistConflictError(BootstrapCfnError):
    def __init__(self, stack_tag):
        msg = ("An {} record already exists. ".format(stack_tag))
        super(TagRecordExistConflictError, self).__init__(msg)


class ActiveTagExistConflictError(BootstrapCfnError):
    def __init__(self, stack_id):
        msg = ("An active record already exists in. ".format(stack_id))
        super(ActiveTagExistConflictError, self).__init__(msg)


class TagRecordNotFoundError(BootstrapCfnError):
    def __init__(self, tag):
        msg = ("Could not find a dns record for tag '{}'. ".format(tag))
        super(TagRecordNotFoundError, self).__init__(msg)


class PublicELBNotFoundError(BootstrapCfnError):
    def __init__(self):
        msg = "Could not find a internet facing ELB. "
        super(PublicELBNotFoundError, self).__init__(msg)


class StackRecordNotFoundError(BootstrapCfnError):
    def __init__(self, stack_record_name):
        msg = ("Could not find a dns record for stack '{}'. ".format(stack_record_name))
        super(StackRecordNotFoundError, self).__init__(msg)
