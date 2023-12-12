// HEAD
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.39.0'
import { load } from 'deps/lib.ts'
//
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2.39.0'
import { load } from 'deps/lib.ts'
//368411653d2ef9656c218c10290baefcb832fd82
const env = await load()
const SUPABASE_URL = env['SUPABASE_URL']
const SUPABASE_KEY = env['SUPABASE_KEY']
// HEAD
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)

export default supabase
//
const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)

export default supabase
//368411653d2ef9656c218c10290baefcb832fd82
