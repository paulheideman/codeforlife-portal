/*
Code for Life

Copyright (C) 2015, Ocado Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
$(function() {
    var updateFunction = (PASSWORD_TYPE == 'STUDENT') ? updateStudentPasswordStrength : updateTeacherPasswordStrength;

    password_field = $('#' + PASSWORD_FIELD_ID);
    password_field.on('keydown', updateFunction);
    password_field.on('paste', updateFunction);
    password_field.on('cut', updateFunction);
    updateFunction();
});

var teacher_password_strengths = [
    { name: 'Password quality', colour: '' },
    { name: 'Poor quality', colour: '#FF0000' },
    { name: 'Not quite', colour: '#DBA901' },
    { name: 'Nearly there', colour: '#D7DF01' },
    { name: 'Good password', colour: '#088A08' }
];

function updateTeacherPasswordStrength() {
    // The reason for the timeout is that if we just got $('#...').val() we'd get the
    // old value before the keypress / change. Apparently even jQuery itself implements
    // things this way, so maybe there is no better workaround.

    setTimeout(function() {
        var password = $('#' + PASSWORD_FIELD_ID).val();

        var strength = 4;
        if (password.length < 8) { strength--; }
        if (password.search(/[A-Z]/) === -1) { strength--; }
        if (password.search(/[a-z]/) === -1) { strength--; }
        if (password.search(/[0-9]/) === -1) { strength--; }

        if (password == '') { $('.password-strength-bar-container').hide(); $('.password-strength-text').hide(); }
        else { $('.password-strength-bar-container').show(); $('.password-strength-text').show(); }

        $('.password-strength-bar').css('width', strength / 4 * 100 + '%');
        $('.password-strength-bar').css('background-color', teacher_password_strengths[strength].colour);
        $('.password-strength-text').html(teacher_password_strengths[strength].name);
    });
}

var student_password_strengths = [
    { name: 'Password quality', colour: '' },
    { name: 'Not long enough', colour: '#DBA901' },
    { name: 'Good password', colour: '#088A08' }
];

function updateStudentPasswordStrength() {
    setTimeout(function() {
        var password = $('#' + PASSWORD_FIELD_ID).val();

        var strength = 0;
        if (password == '') { strength = 0; }
        else if (password.length < 6) { strength = 1; }
        else if (password.length >= 6) { strength = 2; }

        if (password == '') { $('.password-strength-bar-container').hide(); $('.password-strength-text').hide(); }
        else { $('.password-strength-bar-container').show(); $('.password-strength-text').show(); }

        $('.password-strength-bar').css('width', strength / 2 * 100 + '%');
        $('.password-strength-bar').css('background-color', student_password_strengths[strength].colour);
        $('.password-strength-text').html(student_password_strengths[strength].name);
    });
}