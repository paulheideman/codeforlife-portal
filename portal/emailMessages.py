# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from django.core.urlresolvers import reverse


def emailSubjectPrefix():
    return 'Code for Life'


def emailBodySignOff(request):
    return '\n\nThanks,\n\nThe Code for Life team.\n' + request.build_absolute_uri(reverse('home'))


def emailVerificationNeededEmail(request, token):
    return {
        'subject': emailSubjectPrefix() + " : Email address verification needed",
        'message': ("Please go to "
                    + request.build_absolute_uri(reverse('verify_email', kwargs={'token': token}))
                    + " to verify your email address" + emailBodySignOff(request)),
    }


def emailChangeVerificationEmail(request, token):
    return {
        'subject': emailSubjectPrefix() + " : Email address verification needed",
        'message': ("You are changing your email, please go to "
                    + request.build_absolute_uri(reverse('verify_email', kwargs={'token': token}))
                    + " to verify your new email address. If you are not part of Code for Life "
                    + "then please ignore this email. " + emailBodySignOff(request)),
    }


def emailChangeNotificationEmail(request, new_email):
    return {
        'subject': emailSubjectPrefix() + " : Email address changed",
        'message': ("Someone has tried to change the email address of your account. If this was "
                    + "not you, please get in contact with us via "
                    + request.build_absolute_uri(reverse('contact')) + "."
                    + emailBodySignOff(request)),
    }


def joinRequestPendingEmail(request, pendingAddress):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request pending",
        'message': ("Someone with the email address '" + pendingAddress
                    + "' has asked to join your school or club, please go to "
                    + request.build_absolute_uri(reverse('organisation_manage'))
                    + " to view the pending join request." + emailBodySignOff(request)),
    }


def joinRequestSentEmail(request, schoolName):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request sent",
        'message': ("Your request to join the school or club '" + schoolName
                    + "' has been sent. Someone will either accept or deny your request soon."
                    + emailBodySignOff(request)),
    }


def joinRequestAcceptedEmail(request, schoolName):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request accepted",
        'message': ("Your request to join the school or club '" + schoolName
                    + "' has been accepted." + emailBodySignOff(request)),
    }


def joinRequestDeniedEmail(request, schoolName):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request denied",
        'message': ("Your request to join the school or club '" + schoolName
                    + "' has been denied. If you think this was in error you should speak to the "
                    + "administrator of that school or club." + emailBodySignOff(request)),
    }


def kickedEmail(request, schoolName):
    return {
        'subject': emailSubjectPrefix() + " : You were removed from your school or club",
        'message': ("You have been removed from the school or club '" + schoolName
                    + "'. If you think this was in error, please contact the administrator of that "
                    + "school or club."),
    }


def adminGivenEmail(request, schoolName):
    return {
        'subject': emailSubjectPrefix() + " : You have been made a school or club administrator",
        'message': ("Administrator control of the school or club '" + schoolName
                    + "' has been given to you. Go to "
                    + request.build_absolute_uri(reverse('organisation_manage'))
                    + " to start managing your school or club." + emailBodySignOff(request)),
    }


def adminRevokedEmail(request, schoolName):
    return {
        'subject': emailSubjectPrefix() + " : You are no longer a school or club administrator",
        'message': ("Your administrator control of the school or club '" + schoolName
                    + "' has been revoked. If you think this is in error, please contact one of "
                    + "the other administrators in your school or club."
                    + emailBodySignOff(request)),
    }


def contactEmail(request, name, telephone, email, message, browser):
    return {
        'subject': emailSubjectPrefix() + " : Contact from Portal",
        'message': (("The following message has been submitted on the Code for Life portal:"
                    + "\n\nName: {name}\nTelephone: {telephone}\nEmail: {email}\n\nMessage:"
                    + "\n{message}\n\nBrowser version data received:\n{browser}").format(
                    name=name, telephone=telephone, email=email, message=message, browser=browser)),
    }


def confirmationContactEmailMessage(request, name, telephone, email, message):
    return {
        'subject': emailSubjectPrefix() + " : Your message has been sent",
        'message': ("Your message has been sent to our Code for Life team who will get back to you "
                    + "as soon as possible.\n\nYour message is shown below."
                    + emailBodySignOff(request)
                    + ("\n\nName: {name}\nTelephone: {telephone}\nEmail: {email}\n\nMessage:"
                       + "\n{message}").format(
                        name=name, telephone=telephone, email=email, message=message)),
    }


def studentJoinRequestSentEmail(request, schoolName, accessCode):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request sent",
        'message': ("Your request to join the school or club '" + schoolName + "' in class "
                    + accessCode + " has been sent to that class's teacher, who will either accept "
                    + "or deny your request." + emailBodySignOff(request)),
    }


def studentJoinRequestNotifyEmail(request, username, email, accessCode):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request by student " + username,
        'message': ("There is a request waiting from student with username '" + username
                    + "' and email " + email + " to join your class " + accessCode + ". Go to "
                    + request.build_absolute_uri(reverse('teacher_classes'))
                    + " to review the request." + emailBodySignOff(request)),
    }


def studentJoinRequestRejectedEmail(request, schoolName, accessCode):
    return {
        'subject': emailSubjectPrefix() + " : School or club join request rejected",
        'message': ("Your request to join the school or club '" + schoolName + "' in class "
                    + accessCode + " has been rejected. Speak to your teacher if you think this is "
                    + "in error." + emailBodySignOff(request)),
    }
